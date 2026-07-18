import subprocess


def main():
    subprocess.run(["pytest", "--alluredir=reports/allure-results"], check=False)


if __name__ == "__main__":
    main()
