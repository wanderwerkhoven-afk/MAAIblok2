"""Provider-neutral placeholder for student model integrations."""


class StudentLLMClient:
    """Callable adapter students can connect to their own language model.

    Implement :meth:`__call__` with the provider and authentication available to
    your project. The summarizer and corruption workflow only depend on this small
    asynchronous interface, so provider-specific code stays in this class.
    """

    async def __call__(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        max_completion_tokens: int,
    ) -> str:
        """Generate text from the supplied prompts using a student-selected model.

        Args:
            system_prompt: Instructions describing the task and output constraints.
            user_prompt: Report evidence or summary text to process.
            max_completion_tokens: Maximum response length requested from the model.

        Returns:
            Generated response text as a string.

        Raises:
            NotImplementedError: Until a student adds a provider implementation.
        """
        # Student implementation: create or reuse your provider's async client.
        # Send both prompts, apply the token limit, and return generated text only.
        raise NotImplementedError(
            "Connect StudentLLMClient.__call__ to a language-model provider before "
            "running summary or corruption generation."
        )

    async def close(self) -> None:
        """Release provider resources when the notebook workflow is closed.

        Override this method if the provider client owns sessions or connections.

        Returns:
            None: No resources are held by the placeholder implementation.
        """
