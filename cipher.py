import onetimepad
cipher = onetimepad.encrypt('cipher text is this', 'random')
print("cipher text is :")
print(cipher)
print("plain text is:")
msg = onetimepad.decrypt(cipher,'random')
print(msg)
