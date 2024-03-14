from langchain_core.callbacks.base import BaseCallbackHandler
from langchain.agents.agent import AgentAction
from typing import Any, Union


class RetryCallbackHandler(BaseCallbackHandler):
    def on_tool_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> Any:
        # Log the error or perform any necessary actions

        # Retry logic
        max_retries = 1
        current_retry = kwargs.get("retry_count", 0)
        if current_retry < max_retries:
            print(f"Retrying tool execution (Attempt {current_retry + 1})")
            # Increment retry count
            kwargs["retry_count"] = current_retry + 1
            # Re-run the tool
            return AgentAction.RERUN
        else:
            print("Maximum retries reached. Switching to another tool.")
            return AgentAction.CHANGE_TOOL
