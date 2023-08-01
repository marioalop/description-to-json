from abc import ABC, abstractmethod


class LangChainInterface(ABC):
    """
    Interface for the LangChain.
    """

    @abstractmethod
    def generate(self, description: str) -> str:
        """
        Generate a rule based on a description.

        Parameters
        ----------
        description : str
            Any description of any thing to generate.

        Returns
        -------
        str
            The generated String.
        """
        pass
