import base64

encode_byte = base64.b64encode('base64加密'.encode('utf-8'))
print(encode_byte)
encode_str = base64.b64encode('base64加密'.encode('utf-8')).decode('utf-8')
print(encode_str)
decode_byte = base64.b64decode(encode_byte).decode('utf-8')
print(decode_byte)
decode_str = base64.b64decode(encode_str)
print(decode_byte)