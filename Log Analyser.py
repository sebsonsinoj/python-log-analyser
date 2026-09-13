def analyse_log(file_name):
    success = 0
    failed = 0
    ips = {}

    try:
        with open(file_name, "r") as file:

            for line in file:
                if "LOGIN SUCCESS" in line:
                    success += 1

                if "LOGIN FAILED" in line:
                    failed += 1

                words = line.split()

                for word in words:
                    if word.startswith("IP:"):
                        ip = word[3:]

                        if ip in ips:
                            ips[ip] += 1
                        else:
                            ips[ip] = 1

        print("\n===== LOG ANALYSER =====")
        print("Successful logins:", success)
        print("Failed logins:", failed)

        print("\nIP addresses:")

        for ip in ips:
            print(ip, "-", ips[ip], "attempts")

        print("\nIP addresses with multiple attempts:")

        found = False

        for ip in ips:
            if ips[ip] > 3:
                print(ip, "-", ips[ip], "attempts")
                found = True

        if not found:
            print("None found.")

    except FileNotFoundError:
        print("File could not be found.")


file_name = input("Enter the log file name: ")

analyse_log(file_name)
