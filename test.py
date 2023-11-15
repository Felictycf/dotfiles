import base64
import itertools

def xor_bruteforce(data):
    for key in range(256):
        decoded_data = ''.join(chr(b ^ key) for b in data)
        if all(32 <= ord(c) <= 126 or c == '\n' for c in decoded_data):
            print(f"Key: {key}, Decoded data: {decoded_data}")

encoded_data = '''JyM9IiM9ISAqPSEiKzx5emBnPXlg
ISElPSEjIj0iJCA9JCE8e3x8d2R6fXg8RXJ9cHxmZXZhPGV6YHpnPGBmfn52YT17Z35/
ISMjPSInJz0mIz0hIiE8YXZgcn5jf3Z3PHF2dXxhdj17Z35/
ISEiPSIlJj0iJSc9JiU8Y2Z/f3FycHg8anZge3plcns9Z2tn
JyY9IiYiPSIrID0iJyo8eHJge3ZhPEt2YXxren10PXlg
ISEkPSEhPSImJD0mPGZgcjxgfHBwdmE9e2d+fw==
ISIrPSIiID0iJCs9JCI8ZHZyZ3t2YT17Z35/
IiQrPSsmPSIqIj0mITx2dmNhfH48YHZldmF2PXtnfn8=
IiMiPSogPSohPSIlJDx8YGd2fWB8YWo8ZHpweHZ3PHJ/fw==
IiA9KyE9IiYiPSEiJjx/fGNjdmE8d2Z+cXF2f389Z2tn
KiM9ICY9ISAnPSEnKzx8YXp2fWc8cXJ4dmFgPXtnfn8=
IiMmPSQiPSEgJD0iJTxgZmN2YTxwf3JxcXZhYD1rfn8=
ICE9ISc9IScrPSIkKzx0fHx3emB7PHV2f398ZD17Z35/
IiMrPSIiJj0qKj0rJTxqdn9/fGR7cn5+dmE8YXZjfGFnYA==
IiErPSIgJz0iJCU9IiElPHZremBnYDxDcmByd3Z9cj13fHA=
JSQ9KyY9IScrPSEmPGRyenVgPHlmfXw9e2d+fw==
ISMhPSIqPSIqJD0iICI8fHBnfHF2YTxgcmdmYX09eWA=
IiYqPSEgIT0iIyE9IiYrPGNyYGB6fXQ8YHxmYXB2PHt8fnY9cmBj
IiUlPSEjPSYgPSEiKjxRZmFxcn14PF9mcHp3PHlycHhgPXtnfn8=
IiclPSshPSQkPSYqPGAqIioiIjx4f2B5ciIiPHV6f2d2YT1na2c=
ISAgPSIkIT0iKyM9IiUgPGFyfXB7dmE8ZHp9d3xkYD1je2M=
ISYhPSEhKj0iKiA9ISEkPGBnfHB4PGdhcnd6fXQ9e2d+fw==
ISIhPScgPSInIz0iJiE8YGN8YWc8e3Jje3JpcmF3PXlg
IisnPScrPSInID0iIiQ8ZHJ6Z3p9dD1yYGM=
ISYgPSEhJz0iJCI9ICo8fXZkYDxwfH5+PWN7Yw==
Jic9IiAqPSIrIz0iICs8YXxyYWA8ZXJhenxmdzxyf2d2YX1yZ3p8fT17Z35/
IiUrPSsnPSIqKz0hJys8YHZ2fTxqdn9jPXtnfn8=
IismPSEhKj0iJiQ9IiUrPHx9YXZwanZ7fDxldmFxcn89Z2tn
ISEqPSY9ISAgPSEjJDxndnpqajxgY39meD1yYGM=
IionPSEjKj0rKj0nIjxgdmF6fGA8e3J/cXZhPXtnfn8='''
decoded_data = base64.b64decode(encoded_data)

xor_bruteforce(decoded_data)

