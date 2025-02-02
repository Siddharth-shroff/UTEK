# UTEK Emergency Response System

This project is designed to develop an automated disaster response system that can quickly send emergency alerts and prioritize citizen needs in a disaster scenario using Twilio for communication.

## Overview

When the user sends 'help' to the Twilio number, a series of questions is triggered. When the user sends 'help' to the Twilio number, a series of questions is started. The system collects information from the user: how severe their injuries are, their age, and their location. It then sends an emergency message to nearby dispatch centers with responders. The system also prioritizes the emergency response based on the injuries and the user's proximity to the incident.

## Features

- **Interactive Help Process**: When 'help' is sent to the Twilio number, a series of questions is triggered to gather user information. 
- **Automated Message Sending**: Rescuers from the dispatch center are then notified to assist the user based on the gathered data.
- **Google Sheets Integration**: Stores and retrieves user and dispatch center data using Google Sheets, providing a centralized and accessible data repository.
- **Priority-based Dispatch**: The system calculates and prioritizes emergency responses based on citizen injury severity and proximity to dispatch centers.

### `HQDetails.py`
- **Purpose**: Manages data for response/dispatch centers.
- **Key Features**:
  - Stores details for each dispatch center, including:
    - Number of each type of emergency vehicle.
    - Number of each type of emergency response office.
    - Location of the center.
  - Accepts input as a string list containing these attributes.

### `UserDetails.py`
- **Purpose**: Manages data for citizens requiring emergency services.
- **Key Features**:
  - Stores details for each citizen in need, including:
    - Type of injury.
    - Age range.
    - Location.
  - Accepts input as a string list containing these attributes.

### `main.py`
- **Purpose**: Core system for prioritization and calculations.
- **Key Features**:
  - Calculates:
    - Distance from the user to the fire or emergency.
    - Closest dispatcher to the user.
    - Priority of each user based on their emergency needs.
  - Contains all major functions and methods for the system.

### `text_message.py`
- **Purpose**: Handles communication via text messages using Twilio.
- **Key Features**:
  - Receives, reads, and responds to text messages.
  - If the sender texts "help," the system:
    - Gathers information about the sender, including age, name, injury type, and location, through repeated text messages

## Installation

1. Install the required libraries:

```bash
pip install twilio
pip install twilio gspread google-auth
```

## References

[1] “Receive and Reply to Incoming Messages - Python | Twilio,” Twilio.com, 2025. [Link](https://www.twilio.com/docs/messaging/tutorials/how-to-receive-and-reply/python#code-respond-to-an-incoming-text-message) (accessed Jan. 18, 2025).

[2] H. Canada, “Human health effects of wildfire smoke,” canada.ca, Jun. 06, 2024. [Link](https://www.canada.ca/en/health-canada/services/publications/healthy-living/human-health-effects-wildfire-smoke.html).

[3] “What to Expect When You Call 9-1-1,” Londonpolice.ca, 2024. [Link](https://www.londonpolice.ca/en/services/what-to-expect-when-you-call-911.aspx#What-to-expect-when-you-call-9-1-1) (accessed Jan. 18, 2025).

[4] “How to Talk to Emergency Dispatcher | Calling 911,” Minutes Matter, Jan. 10, 2020. [Link](https://minutesmatter.upmc.com/how-to-talk-to-the-emergency-dispatcher/).

[5] S. Valdarrama, “Sorting Algorithms in Python,” Realpython.com, Apr. 15, 2020. [Link](https://realpython.com/sorting-algorithms-python/#pythons-built-in-sorting-algorithm) (accessed Jan. 18, 2025).

[6] St. Mary's Regional Medical Center, “Emergency Care — What to Expect,” St. Mary’s Regional Medical Center, Apr. 28, 2016. [Link](https://www.stmarysregional.com/services/emergency-services/emergency-care-what-to-expect).

[7] P. Canadian, “Prehospital CTAS Paramedic Guide Prehospital CTAS Paramedic Guide Emergency Health Services Branch Ministry of Health and Long-Term Care.” Available: [Link](https://files.ontario.ca/moh_3/moh-manuals-prehospital-ctas-paramedic-guide-v2-0-en-2016-12-31.pdf).

[8] “gspread — gspread 6.1.3 documentation,” Gspread.org, 2024. [Link](https://docs.gspread.org/en/v6.1.3/) (accessed Jan. 18, 2025).

[9] “google.oauth2.service_account module — google-auth 1.30.0 documentation,” Readthedocs.io, 2021. [Link](https://google-auth.readthedocs.io/en/master/reference/google.oauth2.service_account.html) (accessed Jan. 18, 2025).

[10] D. Lee, “Los Angeles residents grapple with long recovery as firefighters make gains in wildfire battle,” CNN, Jan. 17, 2025. Available: [Link](https://www.cnn.com/weather/live-news/fires-los-angeles-california-01-17-25/index.html). [Accessed: Jan. 18, 2025]
