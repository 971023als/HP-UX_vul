#!/usr/bin/python3
import subprocess
import re
import json

def check_sendmail_version_aix():
    results = {
        "분류": "서비스 관리",
        "코드": "U-30",
        "위험도": "상",
        "진단 항목": "Sendmail 버전 점검 (AIX)",
        "진단 결과": None,
        "현황": [],
        "대응방안": "Sendmail 버전을 최신 버전으로 유지"
    }

    latest_version = "8.17.1"  # 최신 Sendmail 버전 예시

    # AIX에서 Sendmail 버전 확인
    cmd = "lslpp -L | grep -i 'sendmail'"
    process = subprocess.run(cmd, shell=True, text=True, capture_output=True)

    sendmail_version = ""
    if process.returncode == 0 and process.stdout:
        sendmail_version_match = re.search(r'sendmail\s+(\d+\.\d+\.\d+)', process.stdout)
        if sendmail_version_match:
            sendmail_version = sendmail_version_match.group(1)

    # 버전 비교 및 결과 설정
    if sendmail_version:
        if sendmail_version.startswith(latest_version):
            results["진단 결과"] = "양호"
            results["현황"].append(f"Sendmail 버전이 최신 버전({latest_version})입니다.")
        else:
            results["진단 결과"] = "취약"
            results["현황"].append(f"Sendmail 버전이 최신 버전({latest_version})이 아닙니다. 현재 버전: {sendmail_version}")
    else:
        results["진단 결과"] = "양호"
        results["현황"].append("Sendmail이 설치되어 있지 않습니다.")

    return results

def main():
    results = check_sendmail_version_aix()
    print(json.dumps(results, ensure_ascii=False, indent=4))

if __name__ == "__main__":
    main()

