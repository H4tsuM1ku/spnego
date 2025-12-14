def __getattr__(name):
	match name:
		case "NegTokenInit":
			from .neg_token_init import NegTokenInit
			return NegTokenInit
		case "NegTokenInit2":
			from .neg_token_init2 import NegTokenInit2
			return NegTokenInit2
		case "NegTokenResp":
			from .neg_token_resp import NegTokenResp
			return NegTokenResp

	raise AttributeError(f"module {__name__} has no attribute {name}")