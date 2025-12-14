from spnego.constants import MS_KILE_OID, KRB5_OID, NTLM_OID, SPNEGOEX_OID

from .base import NegToken

class NegTokenInit(NegToken):
	def __init__(self):
		super(NegTokenInit, self).__init__(1)

		self.mechTypes = [
			NTLM_OID
		]
