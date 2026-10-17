import http.server
import socketserver
import time
import datetime

PORT = 8000
# Simulate cold start if the server hasn't received a request for this duration
COLD_START_INACTIVITY_THRESHOLD_SECONDS = 10 
# The simulated delay for a cold start (e.g., container spin-up, code loading)
COLD_START_DELAY_SECONDS = 3 
# A small, typical delay for a warm, ready environment
WARM_RESPONSE_DELAY_SECONDS = 0.1 

last_request_time = None

class ColdStartHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        global last_request_time
        current_time = datetime.datetime.now()
        is_cold_start = False

        # Check if enough time has passed since the last request to trigger a cold start
        if last_request_time is None or \
           (current_time - last_request_time).total_seconds() > COLD_START_INACTIVITY_THRESHOLD_SECONDS:
            is_cold_start = True
            print(f"\n[{current_time.strftime('%H:%M:%S')}] --- COLD START DETECTED ---")
            # Simulate the environment spin-up delay characteristic of a cold start
            time.sleep(COLD_START_DELAY_SECONDS)
            response_message = f"Cold start response after {COLD_START_DELAY_SECONDS} seconds. Server was inactive.\n"
        else:
            # Simulate a fast response from an already warm/active environment
            time.sleep(WARM_RESPONSE_DELAY_SECONDS)
            response_message = f"Warm response after {WARM_RESPONSE_DELAY_SECONDS} seconds. Server was active.\n"

        last_request_time = current_time

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(response_message.encode("utf-8"))
        print(f"[{current_time.strftime('%H:%M:%S')}] Request served: {response_message.strip()}")

print(f"Starting server on port {PORT}")
print(f"Cold start will be simulated if inactive for > {COLD_START_INACTIVITY_THRESHOLD_SECONDS} seconds.")
print(f"Cold start delay: {COLD_START_DELAY_SECONDS}s, Warm response delay: {WARM_RESPONSE_DELAY_SECONDS}s")
print("Access http://localhost:8000/ in your browser or with curl.")
print("Observe the delay on the first request after inactivity.")

with socketserver.TCPServer(('', PORT), ColdStartHandler) as httpd:
    httpd.serve_forever()
