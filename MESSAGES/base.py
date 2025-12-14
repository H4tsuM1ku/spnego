import asn1

from spnego.constants import SPNEGO_OID

class NegToken(object):
	def __init__(self, token_type):
		self.token_type = token_type

		if self.token_type == 1 or self.token_type == 2:
			self.mechTypes		= None
			self.reqFlags		= None
			self.mechToken		= None
		if self.token_type == 2:
			self.negHints		= None
		if self.token_type == 3:
			self.negResult		= None
			self.supportedMech	= None
			self.responseToken	= None

		self.mechListMIC = None


	def to_bytes(self):
		encoder = asn1.Encoder()
		encoder.start()

		if self.token_type == 1 or self.token_type == 2:
			encoder.enter(0, asn1.Types.Constructed | asn1.Classes.Application) # CHOICE { NegTokenInit [0] } \x60\x3c
			encoder.write(SPNEGO_OID, asn1.Numbers.ObjectIdentifier)

			encoder.enter(0, asn1.Types.Constructed | asn1.Classes.Context)
			encoder.enter(asn1.Numbers.Sequence) # NegTokenInit ::= SEQUENCE

			if self.mechTypes:
				encoder.enter(0, asn1.Types.Constructed | asn1.Classes.Context) # mechTypes [0]
				encoder.enter(asn1.Numbers.Sequence) # mechTypes ::= SEQUENCE

				for mechType in self.mechTypes:
					encoder.write(mechType, asn1.Numbers.ObjectIdentifier) # MechType

				encoder.leave()
				encoder.leave()

			if self.reqFlags:
				encoder.enter(1, asn1.Types.Constructed | asn1.Classes.Context) # reqFlags [1]
				encoder.enter(asn1.Numbers.BitString) # reqFlags ::= BIT STRING

				# TODO : implem les bit string

				encoder.leave()
				encoder.leave()

			if self.mechToken:
				encoder.enter(2, asn1.Types.Constructed | asn1.Classes.Context) # mechToken [2]

				encoder.write(self.mechToken, asn1.Numbers.OctetString)

				encoder.leave()

			try:
				if self.negHints:
					encoder.enter(3, asn1.Types.Constructed | asn1.Classes.Context) # negHints [3]
					encoder.enter(asn1.Numbers.Sequence) # negHints ::= SEQUENCE

					if self.negHints.hintName:
						encoder.enter(0, asn1.Types.Constructed | asn1.Classes.Context) # hintName [0]

						encoder.write(self.negHints.hintName, asn1.Numbers.GeneralString)


						encoder.leave()

					if self.negHints.hintAddress:
						encoder.enter(1, asn1.Types.Constructed | asn1.Classes.Context) # hintAddress [1]

						encoder.write(self.negHints.hintName, asn1.Numbers.OctetString)

						encoder.leave()

					encoder.leave()
					encoder.leave()
			except:
				x = 0
			else:
				x = 1

			if self.mechListMIC:
				encoder.enter(3 + x, asn1.Types.Constructed | asn1.Classes.Context) # mechListMIC [3|4]

				encoder.write(self.mechListMIC, asn1.Numbers.OctetString)

				encoder.leave()

			encoder.leave()
			encoder.leave()
			encoder.leave()

		return encoder.output()

	@classmethod
	def from_bytes(cls):
		pass