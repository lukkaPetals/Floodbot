import pyautogui
import time
arroba = str(input("Cole o @ da pessoa que você quer invocar: "))
quant = int(input(f"Digite quantas vezes você quer marcar {arroba}: "))
print("O bot ira funcionar daqui 5 segundos aguarde...")
time.sleep(5)
print("O bot está funcionando no momento")
for c in range(0, quant):
    pyautogui.typewrite(arroba)
    time.sleep(0.3)
    for d in range(0, 3):
        pyautogui.press("enter")
