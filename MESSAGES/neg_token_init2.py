from spnego.constants import MS_KILE_OID, KRB5_OID, KRB5_U2U_OID, NTLM_OID, SPNEGOEX_OID
from spnego.STRUCTURES import NegHints

from .base import NegToken

class NegTokenInit2(NegToken):
	def __init__(self):
		super(NegTokenInit2, self).__init__(2)

		self.mechTypes = [
			SPNEGOEX_OID,
			MS_KILE_OID,
			KRB5_OID,
			KRB5_U2U_OID,
			NTLM_OID
		]

		self.negHints = NegHints()