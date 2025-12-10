import asn1
import struct

def OID_to_bytes(OID):
	encoder = asn1.Encoder()
	encoder.start()
	encoder.write(OID, asn1.Numbers.ObjectIdentifier)
	encoded_bytes = encoder.output()

	return encoded_bytes

def bytes_to_OID(OID_bytes):
	decoder = asn1.Decoder()
	decoder.start(encoded_bytes)
	tag, OID = decoder.read()

	return OID