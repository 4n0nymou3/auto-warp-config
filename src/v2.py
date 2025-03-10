import json
import random
import requests

def fetch_ips():
    try:
        response = requests.get('https://raw.githubusercontent.com/ircfspace/endpoint/refs/heads/main/ip.json')
        data = response.json()
        return data
    except Exception as e:
        return {
            "ipv4": ["162.159.192.23:859", "162.159.192.178:4500"],
            "ipv6": ["[2606:4700:d1::9f62:b405:88e4:858e]:7152"]
        }

def update_config_file(config_file):
    try:
        with open(config_file, 'r') as f:
            data = json.load(f)

        ips = fetch_ips()
        ipv4_list = random.sample(ips['ipv4'], 2)
        ipv6 = random.choice(ips['ipv6'])

        # انتخاب تصادفی از IPهای IPv4 و IPv6
        new_endpoint = random.choice(ipv4_list + [ipv6])

        # تغییر endpoint در فایل JSON
        data['outbounds'][0]['settings']['peers'][0]['endpoint'] = new_endpoint

        with open(config_file, 'w') as f:
            json.dump(data, f, indent=2)

        print(f"Endpoint به {new_endpoint} تغییر یافت.")

    except FileNotFoundError:
        print(f"خطا: فایل {config_file} یافت نشد.")
    except json.JSONDecodeError:
        print(f"خطا: فایل {config_file} یک فایل JSON معتبر نیست.")
    except KeyError:
        print("خطا: ساختار فایل JSON مطابق انتظار نیست.")

if __name__ == "__main__":
    config_file = 'oop.txt'  # نام فایل JSON شما
    update_config_file(config_file)
