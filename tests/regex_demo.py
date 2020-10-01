# stdlib
import re

no_flags = re.compile(r"Hello\s+[Ww]orld[.,](Lovely|Horrible) weather, isn't it (.*)\?")
one_flag = re.compile(r"Hello\s+[Ww]orld[.,](Lovely|Horrible) weather, isn't it (.*)\?", flags=re.IGNORECASE)
two_flags = re.compile(
		r"Hello\s+[Ww]orld[.,](Lovely|Horrible) weather, isn't it (.*)\?", flags=re.ASCII | re.DEBUG
		)