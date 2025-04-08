# Email Sending Tracker

This Python script helps manage and track email outreach efforts by maintaining a **master list** of email addresses and a **sent list** of addresses that have already received emails. It generates a daily list of up to 50 new email addresses to contact and updates the records accordingly.

---

## 📁 Files Used

- `master_list.csv`: A CSV file containing the full list of email addresses.
- `sent_list.csv`: A CSV file that tracks which addresses have already been emailed.

---

## 📂 Files Created

- `send_list_YYYY-MM-DD.txt`: The list of up to 50 new email addresses selected for today's outreach.
- `sent_list_YYYY-MM-DD.txt`: A backup of the updated `sent_list` as of today.
- **(Updated)** `sent_list.csv`: Overwritten after each run to reflect all sent emails.

---

## 🚀 How to Use

1. Make sure your `master_list.csv` is in the same folder as the script.
2. Run the script using Python 3:

   ```bash
   python email_tracker.py
