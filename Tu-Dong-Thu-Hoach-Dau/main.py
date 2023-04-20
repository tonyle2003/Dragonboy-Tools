import time
import pyautogui
import keyboard

accounts = {
    "account1": "password1",
    "account2": "password2",
    "account3": "password3"
}

pyautogui.press('win')
time.sleep(1)
pyautogui.write('Dragonboy_vn_v230')
pyautogui.write('.exe')
time.sleep(1)
pyautogui.press('enter')
print('Đã mở game')
time.sleep(6)
pyautogui.press('enter')
print('Đã nhấn enter')
time.sleep(3.5)
pyautogui.press('enter')
print('Đã nhấn enter')
time.sleep(1)
pyautogui.press('f1')
print('Đã nhấn f1')
pyautogui.press('left')
print('Đã nhấn left')
pyautogui.press('up')
print('Đã nhấn up')
pyautogui.press('enter')
print('Đã nhấn enter')
time.sleep(1)

for username, password in accounts.items():
    pyautogui.press('down')
    print('Đã nhấn down')
    for i in range(0, 30):
        pyautogui.press('backspace')
    pyautogui.write(password)
    print('Đã nhập mật khẩu')
    pyautogui.press('down')
    print('Đã nhấn down')
    for i in range(0, 30):
        pyautogui.press('backspace')
    pyautogui.write(username)
    print('Đã nhập tên tài khoản')
    pyautogui.press('enter')
    print('Đã nhấn enter')
    pyautogui.press('enter')
    print('Đã nhấn enter')
    time.sleep(3.5)
    pyautogui.press('enter')
    print('Đã nhấn enter')
    pyautogui.press('enter')
    print('Đã nhấn enter')
    time.sleep(1)
    pyautogui.press('enter')
    print('Đã thu hoạch đậu')
    time.sleep(1)
    # thoát game
    pyautogui.press('f1')
    print('Đã nhấn f1')
    pyautogui.press('left')
    print('Đã nhấn left')
    pyautogui.press('up')
    print('Đã nhấn up')
    pyautogui.press('enter')
    print('Đã thoát game')
    time.sleep(1)

keyboard.press_and_release('alt + f4')
print('Đã tắt cửa sổ game')