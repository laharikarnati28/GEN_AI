
import unittest

from llm_client import LLMProvider, LLMClient


class FakeProvider(LLMProvider):

    def generate(self, prompt):
        return "Fake response"


class TestLLMClient(unittest.TestCase):

    def test_generate(self):
        provider = FakeProvider()
        client = LLMClient(provider)

        result = client.generate("Hello")

        self.assertEqual(result, "Fake response")


if __name__ == "__main__":
    unittest.main()
