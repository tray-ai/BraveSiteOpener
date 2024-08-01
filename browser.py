import webbrowser, time

def open_browser(sites):
    """Opens each URL in the provided list using a web browser."""

    # Provide path to register brave browser.
    brave_path = ("/Users/deshaud/Desktop/Brave Browser.app"
    "/Contents/MacOS/Brave Browser")

    # Register the browser to use for opening sites.
    webbrowser.register('brave', None,
                        webbrowser.BackgroundBrowser(brave_path))
    
    # Loop through list, and open sites.
    for site in sites:
        webbrowser.get('brave').open(site)
        time.sleep(0.5)

# Initiate the list of URLs.
urls = ['www.chatgpt.com/g/g-cKXjWStaE-python',
       'www.linkedin.com/in/tray-jobe', 
       'www.youtube.com', 
       'www.github.com/tray-ai', ]

open_browser(urls)