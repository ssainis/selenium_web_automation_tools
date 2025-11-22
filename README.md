# Selenium Web Automation Tools

A Python package for creating Selenium-based web automation workflows using [PocketFlow](https://pypi.org/project/pocketflow/).

> **Created by Antigravity**

## Installation

```bash
pip install selenium_web_automation_tools
```

## Usage

This package provides `CustomScraper` and `CustomInputter` nodes that can be used in PocketFlow workflows.

### Example

```python
from pocketflow import Flow
from selenium_web_automation_tools.custom_scraper import CustomScraper

# Create a flow
flow = Flow("My Automation Flow")

# Create a scraper node
scraper = CustomScraper(
    name="MyScraper",
    url="https://example.com",
    description="Scrape the main title"
)

# Add to flow
flow.add_node(scraper)

# Run
flow.run(shared={})
```

### CustomInputter Example

```python
from pocketflow import Flow
from selenium_web_automation_tools.custom_inputter import CustomInputter

# Create a flow
flow = Flow("Login Automation")

# Create an inputter node
inputter = CustomInputter(
    name="LoginForm",
    url="https://example.com/login",
    input_data={
        "username": "myuser",
        "password": "mypassword"
    }
)

# Set as start node
flow = Flow(start=inputter)

# Run
flow.run(shared={})
```

## Demo

See the `demo/` directory for a complete example using a YAML configuration.
