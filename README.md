# UTEK Emergency Response System

This project is designed to develop an automated disaster response system that can quickly send emergency alerts and prioritize citizen needs in a disaster scenario using Twilio for communication.

## Overview

When the user sends 'help' to the Twilio number, a series of questions is triggered. When the user sends 'help' to the Twilio number, a series of questions is started. The system collects information from the user: how severe their injuries are, their age, and their location. It then sends an emergency message to nearby dispatch centers with responders. The system also prioritizes the emergency response based on the injuries and the user's proximity to the incident.

## Features

- **Interactive Help Process**: When 'help' is sent to the Twilio number, a series of questions is triggered to gather user information. 
- **Automated Message Sending**: Rescuers from the dispatch center are then notified to assist the user based on the gathered data.
- **Google Sheets Integration**: Stores and retrieves user and dispatch center data using Google Sheets, providing a centralized and accessible data repository.
- **Priority-based Dispatch**: The system calculates and prioritizes emergency responses based on citizen injury severity and proximity to dispatch centers.

## Installation

1. Install the required libraries:

```bash
pip install twilio
pip install twilio gspread google-auth

