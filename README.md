EC2 instance auto-scheduler project:

```markdown
# 🕒 EC2 Instance Auto Start/Stop using Lambda & EventBridge

Automate stopping and starting EC2 instances based on tags using:
- 🧠 AWS Lambda (Python)
- ⏰ Amazon EventBridge (CloudWatch Events) cron expressions

---

## ✅ Goal

- Stop EC2 instances every night (e.g., **12:00 AM**)
- Start EC2 instances every morning (e.g., **9:00 AM**)
- Target instances based on a **specific tag**:  
  `Key: AutoSchedule` and `Value: true`

---

## 🛠️ Step-by-Step Implementation

### 1. ✅ Tag EC2 Instances

Tag each EC2 instance that you want to schedule:

```

Key:   AutoSchedule
Value: true

````

---

### 2. ✅ Create IAM Role for Lambda

Create an IAM Role with the following policy and attach it to the Lambda function:

---

### 3. ✅ Lambda Function (Python)

---

### 4. ✅ Create EventBridge Rules

#### Rule 1: Stop at Night

* **Name:** `stop-instances-night`
* **Schedule pattern:**
  `cron(0 18 * * ? *)` → Runs at **12:00 AM BD time (6 PM UTC)**
* **Target:** Lambda Function
* **Input:**

```json
{
  "action": "stop"
}
```

---

#### Rule 2: Start in Morning

* **Name:** `start-instances-morning`
* **Schedule pattern:**
  `cron(3 3 * * ? *)` → Runs at **9:03 AM BD time (3:03 AM UTC)**
* **Target:** Lambda Function
* **Input:**

```json
{
  "action": "start"
}
```

---

## 🧪 Optional: Test Manually

You can test the Lambda manually with a test event:

```json
{ "action": "stop" }
```

or

```json
{ "action": "start" }
```

---

## 🧠 Notes

* You can customize the tag key and value as needed.
* Ensure the Lambda timeout is at least **10 seconds**.
* Logs can be viewed in **CloudWatch Logs**.
* Ensure proper IAM permissions are attached.
* Both start/stop rules can target the **same Lambda function** with different input.

---

---
