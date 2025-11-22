import yaml
import sys
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Add the parent directory to sys.path to allow importing from the package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pocketflow import Flow
from selenium_web_automation_tools.custom_scraper import CustomScraper
from selenium_web_automation_tools.custom_inputter import CustomInputter

def load_config(config_path: str) -> dict:
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def main():
    config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    config = load_config(config_path)
    
    nodes = []
    
    for i, step in enumerate(config.get('steps', [])):
        step_type = step.get('type')
        if step_type == 'scrape':
            node = CustomScraper(
                name=f"Step_{i+1}_Scrape",
                url=step['url'],
                description=step['description']
            )
            nodes.append(node)
        elif step_type == 'input':
            node = CustomInputter(
                name=f"Step_{i+1}_Input",
                url=step['url'],
                input_data=step['input_data']
            )
            nodes.append(node)
        else:
            print(f"Unknown step type: {step_type}")
    
    if not nodes:
        print("No steps defined in config.")
        return

    # Chain nodes
    for i in range(len(nodes) - 1):
        nodes[i] >> nodes[i+1]
        
    # Create flow with start node
    flow = Flow(start=nodes[0])
            
    try:
        flow.run(shared={})
        print("Flow execution completed successfully.")
    except Exception as e:
        print(f"Flow execution failed: {e}")

if __name__ == "__main__":
    main()
