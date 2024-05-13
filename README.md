# RepRec

RepRec is a project developed by OE6PGM and OE6UKN to record transmissions occurring on the local repeater. The primary goal is to assess the quality of the sending device by analyzing recorded transmissions. Transmissions are temporarily saved locally and then transmitted to Telegram using the Telegram API.

## Features

- Records transmissions from a local repeater via a microphone input of a USB soundcard.
- Temporarily saves recordings locally.
- Transmits recordings to Telegram via API for easy access and review.
- Automatically starts on Raspberry Pi boot.

## Prerequisites

- Raspberry Pi with a compatible OS.
- Python 3.x.
- Telegram account with API access (Telegram Premium is recommended due to upload limits).

## Setup Instructions

1. **Review Alsa configuration:**

   The setup script copies the ALSA configuration file for your specific use case to the correct system directory. **You might want to review the 'asound.conf' file** located in the 'setup_files' directory before executing the setup script.

2. **Review Service File:**

   The setup script also creates and enables the 'reprec.service' to ensure it starts automatically when the Raspberry Pi boots up. You may need to modify the service file to change directories or the username.

   - **Check the paths and username** in the 'reprec.service' file located in the 'setup_files' directory before executing the setup script.

3. **Run the setup script:**

   Execute the 'setup.sh' script to set up the basic environment. This script will:
   - Install necessary packages for the Raspberry Pi.
   - Create a Python virtual environment.
   - Install the required Python packages.

   ```bash
   ./setup.sh
   ```

4. **Telegram API Setup:**

   The Telegram API requires access to your account. Follow these steps to set it up:
   - Visit [my.telegram.org](https://my.telegram.org/).
   - Under 'API development tools,' obtain your 'api_id' and 'api_hash'.
   - Rename the secrets_template.json to secrets.json and fill out the settings in the file
   - **Note: Telegram Premium is recommended due to upload limits.**

5. **Run the setup script:**

   Execute the 'setup.sh' script to set up the basic environment. This script will:
   - Install necessary packages for the Raspberry Pi.
   - Create a Python virtual environment.
   - Install the required Python packages.

   ```bash
   ./setup.sh
   ```

## Schematic

The recording happens via a microphone device. The schematic for the cable used is available in the `setup_files/diagram_3.5mm_plugs.png` file.

## Usage

Once the setup is complete, the service will automatically start on boot and begin recording transmissions. The recordings will be sent to your configured Telegram account.

## Contributing

If you wish to contribute to the project, please fork the repository and create a pull request. Ensure your code follows the project's coding standards and includes relevant tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Authors

- OE6PGM
- OE6UKN

## Contact

For any questions or support, please contact OE6PGM or OE6UKN.

---

This README file provides an overview of the RepRec project, setup instructions, and usage guidelines. For detailed information, refer to the specific files and scripts mentioned above.

## Schematic

The recording happens via a microphone device. The schematic for the cable used is available in the `setup_files/diagram_3.5mm_plugs.png` file.