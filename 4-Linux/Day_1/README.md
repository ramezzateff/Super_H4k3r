# 🐧 System Info Bash Scripts – Linux Monitoring Toolkit

Welcome to your **System Info Bash Scripting Project**!  
This project includes a set of small, focused Bash scripts that help you collect and monitor system information on any Linux machine.

---

## 📘 Topics Covered

- Distribution and Version Detection  
- User & UID Info  
- Hostname and IP Display  
- Environment Variable Listing  
- Linux OS Check  
- System Uptime Display  
- CPU Info & Core Count  
- RAM Usage (total & free)  
- Architecture Detection (32-bit or 64-bit)  
- Live CPU & Memory Monitoring

---

## 🔹 Scripts Included

| #   | Task Description                                               | File Name                  |
|-----|----------------------------------------------------------------|----------------------------|
| 1️⃣ | Display Linux distribution name and version                    | `0_distro_info.sh`         |
| 2️⃣ | Print current username and its user ID (UID)                  | `1_user_uid.sh`            |
| 3️⃣ | Show system's hostname and local IP address                   | `2_hostname_ip.sh`         |
| 4️⃣ | List all environment variables                                | `3_env_vars.sh`            |
| 5️⃣ | Check if the system is running Linux                          | `4_check_linux.sh`         |
| 6️⃣ | Display system uptime in a readable format                    | `5_uptime.sh`              |
| 7️⃣ | Show CPU model and count number of cores                      | `6_cpu_info.sh`            |
| 8️⃣ | Display total and available RAM (human-readable)              | `7_ram_info.sh`            |
| 9️⃣ | Determine whether the system is 32-bit or 64-bit              | `8_architecture.sh`        |
| 🔟  | Live CPU & Memory usage monitor (real-time)                   | `9_live_monitor.sh`       |

---

## 🛠 Tools Used in Scripts

- `uname`, `hostname`, `whoami`, `id`  
- `ip`, `ifconfig` (optional)  
- `uptime`, `free`, `/proc/cpuinfo`, `/proc/meminfo`  
- `printenv`, `top`, `htop`, `arch`, `lscpu`  

---

## 📎 Notes

- Most scripts are safe and compatible with most Linux distros.  
- For live monitoring, make sure `top` or `htop` is installed.  
- You can run each script separately or combine them into one dashboard.  
- Don’t forget to make each script executable:  
  ```bash
  chmod +x scriptname.sh
