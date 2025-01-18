# UTEK Emergency Response System

This project aims to create an automated disaster response system that can efficiently send emergency alerts and prioritize citizen needs during a disaster scenario using Twilio for communication.

## Overview

When the user sends 'help' to the Twilio number, a series of questions is triggered. The system gathers user information, including injury severity, age, and location, and then sends an emergency message to nearby dispatch centers with responders. The system also prioritizes emergency responses by assessing the severity of injuries and the user's proximity to the incident.

## Features

- **Interactive Help Process**: When 'help' is sent to the Twilio number, a series of questions is triggered to gather user information. 
- **Automated Message Sending**: Rescuers from the dispatch center are then notified and sent a signal to assist the user based on the gathered data.
- **Priority-based Dispatch**: The system calculates and prioritizes emergency responses based on citizen injury severity and proximity to dispatch centers.

## Installation

1. Install the required libraries:

```bash
pip install twilio


