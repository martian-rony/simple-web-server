# Simple Python Web Server with Ngrok

This project demonstrates how to run a basic Python web server locally and expose it to the internet using Ngrok.

## Prerequisites

* Python 3.x installed
* Ngrok installed and configured
* Terminal or Command Prompt access

## Run the Server Locally

Start the server:

```bash
python server.py
```

You should see:

```text
Server running at http://localhost:8000
```

Open your browser and visit:

```text
http://localhost:8000
```

## Install Ngrok

Download Ngrok from:

https://ngrok.com/download

Verify installation:

```bash
ngrok version
```

## Authenticate Ngrok

Sign up for a free Ngrok account and configure your authentication token:

```bash
ngrok config add-authtoken YOUR_AUTH_TOKEN
```

## Expose the Local Server

In a new terminal window, run:

```bash
ngrok http 8000
```

Example output:

```text
Forwarding  https://abc123.ngrok-free.app -> http://localhost:8000
```

## Access from the Internet

Open the generated public URL:

```text
https://abc123.ngrok-free.app
```

Anyone with this URL can access your local web server while Ngrok is running.

## Stopping the Services

### Stop the Python Server

Press:

```text
Ctrl + C
```

### Stop Ngrok

Press:

```text
Ctrl + C
```

## Troubleshooting

### Port Already in Use

If port 8000 is occupied, change the port number in `server.py`:

```python
PORT = 8080
```

Then start Ngrok on the same port:

```bash
ngrok http 8080
```

### Firewall Issues

Ensure local firewall settings allow connections to the selected port.

## Security Notes

* Do not expose sensitive files through the web server.
* The Ngrok URL is publicly accessible.
* Use authentication and HTTPS for production deployments.
* This setup is intended for development, testing, and demonstrations.

## License

MIT License
