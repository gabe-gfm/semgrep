from typing import Any
from typing import Iterable
from typing import Mapping
from typing import Sequence

import semgrep.rpc_call
import semgrep.semgrep_interfaces.semgrep_output_v1 as out
from semgrep.error import SemgrepError
from semgrep.formatter.base import BaseFormatter
from semgrep.formatter.base import to_CliOutput
from semgrep.rule import Rule
from semgrep.rule_match import RuleMatch


class VimFormatter(BaseFormatter):
    def format(
        self,
        rules: Iterable[Rule],
        rule_matches: Iterable[RuleMatch],
        semgrep_structured_errors: Sequence[SemgrepError],
        cli_output_extra: out.CliOutputExtra,
        extra: Mapping[str, Any],
        is_ci_invocation: bool,
    ) -> str:
        output = to_CliOutput(rule_matches, semgrep_structured_errors, cli_output_extra)
        return semgrep.rpc_call.format(out.OutputFormat(out.Vim()), output)
