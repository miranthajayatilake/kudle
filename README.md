<img src="images/logo2.png" alt="Projectlogo" width="200">

![Developer Tool](https://img.shields.io/badge/microsoft%20azure-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/miranthajayatilake/kudle/blob/main/LICENSE)

# Hello there :wave: Welcome to kudle 

**kudle** is an application that helps you deploy docker containers easily on your [Azure Kubernetes Services](https://docs.microsoft.com/en-us/azure/aks/intro-kubernetes) via a graphical user interface in 5 mins! Kudle can be described in just two words, simple and fast :bulb: 

Here's a quick look :eyes: 

<!-- ![](images/gif_capture.gif) -->
<img src="images/gif_capture.gif" alt="gifcapture" width="500">

## Installation

- Clone this repo
- Install the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) locally
- Next install `kubectl` using command `az aks install-cli`
- Set up a python environment with `python >= 3.6`
- Install python dependecies using command `pip install -r requirements.txt`
- Done! Good to run :thumbsup:

## Running kudle

- Make sure you are in the repo directory
- Simply run the `run.sh` file
- Find kudle at the port displayed in terminal (*usually* `http://localhost:8501` :relieved:)

## Using kudle

**When on kudle Interface**

- Login to your azure account using the button if you haven't already
- Expand the **New Kubernetes Deployment** section and fill in the needed details
    - Your Docker image name 
    - Name you want to give your deployment (can be anything)
    - Version number for your deployment

**Azure Configuration Inputs**
- A [Resource group](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal) name (:ballot_box_with_check: if need to create new)
- A [Container registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-intro) name (:ballot_box_with_check: if need to create new)
- A [Kubernetes cluster](https://docs.microsoft.com/en-us/azure/aks/intro-kubernetes) name ((:ballot_box_with_check: if need to create new))

All good! Hit **Deploy** :relieved:
*Information on the status will be displyed below the progress bar*

When completed, expand **Check deployment status** section. Enter your application deployment name again and hit **Get public IP**. If deployed successfully, the public IP for your app will be displayed :clap: :clap: :clap:

## Contributing to kudle
I highly appreciate your contributions to this project in any amount possible. Kudle is still at an very basic stage. Suggestions on additional features and functionality are welcome. General instructions on how to contribute are mentioned in [CONTRIBUTING](CONTRIBUTING.md)

## Getting help
Please use the issues tracker of this repository to report on any bugs or questions you have.

## Upcoming features

- Updating and scaling of running apps