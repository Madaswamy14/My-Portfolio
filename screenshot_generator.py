import argparse
import json
import sys
import time
from pathlib import Path

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
except ImportError:
    print("Error: 'selenium' module is required.")
    print("Please install it using: pip install selenium")
    sys.exit(1)


def setup_driver(headless=True):
    """Initialize a Chrome WebDriver with standard options."""
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    
    # Initialize the driver (assumes chromedriver is in PATH)
    try:
        return webdriver.Chrome(options=chrome_options)
    except Exception as e:
        print(f"Failed to initialize WebDriver: {e}")
        print("Ensure you have a browser driver (like chromedriver) installed and in your PATH.")
        sys.exit(1)


def process_screenshots(config_file, output_dir, headless=True):
    """
    Reads a JSON config file and captures screenshots.
    
    Config format expected:
    [
      { "url": "https://example.com", "output": "example-home.png", "width": 1280, "height": 800 },
      ...
    ]
    """
    config_path = Path(config_file)
    if not config_path.exists():
        print(f"Error: Configuration file not found: {config_file}")
        return

    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            shots = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON config: {e}")
        return

    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    print(f"📸 Starting screenshot session ({len(shots)} items)...")
    driver = setup_driver(headless)

    try:
        for item in shots:
            url = item.get('url')
            filename = item.get('output', 'screenshot.png')
            width = item.get('width', 1920)
            height = item.get('height', 1080)
            
            target_file = out_path / filename
            
            print(f"   Processing: {url} -> {filename}")
            
            # Resize window
            driver.set_window_size(width, height)
            
            # Navigate
            driver.get(url)
            
            # Basic wait for content (in a real app, use WebDriverWait)
            time.sleep(2)
            
            # Save
            driver.save_screenshot(str(target_file))
            
    finally:
        driver.quit()
        print("✅ Session complete.")


def generate_sample_config(path):
    """Helper to create a sample config file."""
    sample = [
        {"url": "https://example.com", "output": "example-desktop.png", "width": 1920, "height": 1080},
        {"url": "https://example.com", "output": "example-mobile.png", "width": 375, "height": 812}
    ]
    with open(path, 'w') as f:
        json.dump(sample, f, indent=2)
    print(f"Created sample config at: {path}")


def main():
    parser = argparse.ArgumentParser(description="Automated Screenshot Generator for Documentation")
    parser.add_argument("--config", default="screenshots.json", help="Path to JSON config file")
    parser.add_argument("--output", default="docs/images", help="Output directory for images")
    parser.add_argument("--init", action="store_true", help="Generate a sample screenshots.json file")
    parser.add_argument("--no-headless", action="store_true", help="Run browser visibly (for debugging)")
    args = parser.parse_args()

    if args.init:
        generate_sample_config(args.config)
    else:
        process_screenshots(args.config, args.output, headless=not args.no_headless)

if __name__ == "__main__":
    main()