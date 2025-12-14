def __getattr__(name):
	match name:
		case "NegHints":
			from .neg_hints import NegHints
			return NegHints

	raise AttributeError(f"module {__name__} has no attribute {name}")