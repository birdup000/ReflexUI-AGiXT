# state.py
import reflex as rx

class SettingsState(rx.State):
    agent_action: str = "Create Agent"
    agent_name_input: str = ""
    agent_name_select: str = ""
    provider_settings: dict = {}
    language_providers: list[str] = ['ProviderA', 'ProviderB', 'ProviderC']
    vision_providers: list[str] = ["None", 'VisionA', 'VisionB']
    tts_providers: list[str] = ["None", 'TTS_A', 'TTS_B']
    stt_providers: list[str] = ['Transcription_A', 'Transcription_B']
    image_providers: list[str] = ["None", 'ImageA', 'ImageB']
    embedding_providers: list[str] = ['EmbeddingsA', 'EmbeddingsB']
    agent_names: list[str] = ['Agent1', 'Agent2', 'Agent3']
    agent_actions: list[str] = ["Create Agent", "Modify Agent", "Delete Agent"]
    selected_language_provider: str = 'ProviderA'
    selected_vision_provider: str = 'None'
    selected_tts_provider: str = 'None'
    selected_stt_provider: str = 'Transcription_A'
    selected_image_provider: str = 'None'
    selected_embedding_provider: str = 'EmbeddingsA'

    def select_agent_action(self, value: str):
        self.agent_action = str(value)

    def set_agent_name_input(self, value: str):
        self.agent_name_input = str(value)

    def set_agent_name_select(self, value: str):
        self.agent_name_select = str(value)

    def set_selected_language_provider(self, value: str):
        self.selected_language_provider = str(value)

    def set_selected_vision_provider(self, value: str):
        self.selected_vision_provider = str(value)

    def set_selected_tts_provider(self, value: str):
        self.selected_tts_provider = str(value)

    def set_selected_stt_provider(self, value: str):
        self.selected_stt_provider = str(value)

    def set_selected_image_provider(self, value: str):
        self.selected_image_provider = str(value)

    def set_selected_embedding_provider(self, value: str):
        self.selected_embedding_provider = str(value)

    def render_provider_settings(self, provider_name: str):
        settings = {
            'provider': '',
            'vision_provider': '',
            'tts_provider': '',
            'transcription_provider': '',
            'image_provider': '',
            'embeddings_provider': ''
        }
        for key in settings.keys():
            if key in self.provider_settings:
                settings[key] = self.provider_settings[key]
            else:
                settings[key] = ""
        self.provider_settings.update(settings)

    def save_agent_settings(self):
        settings = {
            "provider": self.selected_language_provider,
            "vision_provider": self.selected_vision_provider,
            "transcription_provider": self.selected_stt_provider,
            "tts_provider": self.selected_tts_provider,
            "image_provider": self.selected_image_provider,
            "embeddings_provider": self.selected_embedding_provider,
            **self.provider_settings,
        }
        print(f"Settings saved for action: {self.agent_action}")

