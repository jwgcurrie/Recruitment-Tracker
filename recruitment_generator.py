import pandas as pd
from datetime import datetime

# Get today's date
current_date = datetime.now().strftime("%Y-%m-%d")

# --- Load email lists safely ---
def load_email_list(filepath):
    try:
        return pd.read_csv(filepath, header=None).squeeze("columns").dropna().tolist()
    except FileNotFoundError:
        print(f"Warning: {filepath} not found. Starting with an empty list.")
        return []

masterlist = load_email_list('master_list.csv')
sentlist = load_email_list('sent_list.csv')

# --- Filter the emails ---
# 1. Remove already sent emails
sendlist = [email for email in masterlist if email not in sentlist]

# 2. Remove internal IIT emails
filtered_sendlist = [email for email in sendlist if '@iit.it' not in email]

# 3. Select last 50 emails
new_send_list = filtered_sendlist[-50:]

# --- Print info ---
print(f"🟢 {len(new_send_list)} email(s) ready to be sent:")
print(new_send_list)

# --- Save today's send list ---
send_txt_filename = f"send_list_{current_date}.txt"
with open(send_txt_filename, "w") as f:
    f.write(", ".join(new_send_list))
print(f"✅ Send list saved to {send_txt_filename}")

# --- Update sent list ---
updated_sent_list = sorted(set(sentlist + new_send_list))

# Save to today's dated file
sent_txt_filename = f"sent_list_{current_date}.txt"
with open(sent_txt_filename, "w") as f:
    f.write(", ".join(updated_sent_list))
print(f"✅ Sent list saved to {sent_txt_filename}")

# Overwrite sent_list.csv for persistence
pd.Series(updated_sent_list).to_csv('sent_list.csv', index=False, header=False)
print("📦 sent_list.csv has been updated for future runs.")
