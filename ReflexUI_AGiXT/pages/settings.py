# settings.py
from ReflexUI_AGiXT.templates import template
import reflex as rx
from .state import SettingsState

@template(route="/settings", title="Settings")
def settings() -> rx.Component:
    """The settings page.

    Returns:
        The UI for the settings page.
    """
    return rx.vstack(
        rx.heading("Settings", size="8"),
        rx.text("Agent Management", size="6"),
        
        # Agent action selection
        rx.hstack(
            rx.select(
                SettingsState.agent_actions,
                value=SettingsState.agent_action,
                on_change=SettingsState.select_agent_action,
            ),
            rx.cond(
                SettingsState.agent_action == "Create Agent",
                rx.input(
                    value=SettingsState.agent_name_input,
                    on_change=SettingsState.set_agent_name_input,
                    placeholder="Enter agent name",
                ),
                rx.select(
                    SettingsState.agent_names,
                    value=SettingsState.agent_name_select,
                    on_change=SettingsState.set_agent_name_select,
                ),
            ),
        ),
        
        # Language Provider Selection
        rx.hstack(
            rx.text("Language Provider: "),
            rx.select(
                SettingsState.language_providers,
                value=SettingsState.selected_language_provider,
                on_change=SettingsState.set_selected_language_provider,
            ),
        ),
        
        # Vision Provider Selection
        rx.hstack(
            rx.text("Vision Provider (Optional): "),
            rx.select(
                SettingsState.vision_providers,
                value=SettingsState.selected_vision_provider,
                on_change=SettingsState.set_selected_vision_provider,
            ),
        ),
        
        # Text to Speech Provider Selection
        rx.hstack(
            rx.text("Text to Speech Provider: "),
            rx.select(
                SettingsState.tts_providers,
                value=SettingsState.selected_tts_provider,
                on_change=SettingsState.set_selected_tts_provider,
            ),
        ),
        
        # Speech to Text Provider Selection
        rx.hstack(
            rx.text("Speech to Text Provider: "),
            rx.select(
                SettingsState.stt_providers,
                value=SettingsState.selected_stt_provider,
                on_change=SettingsState.set_selected_stt_provider,
            ),
        ),
        
        # Image Generation Provider Selection
        rx.hstack(
            rx.text("Image Generation Provider (Optional): "),
            rx.select(
                SettingsState.image_providers,
                value=SettingsState.selected_image_provider,
                on_change=SettingsState.set_selected_image_provider,
            ),
        ),
        
        # Embeddings Provider Selection
        rx.hstack(
            rx.text("Embeddings Provider: "),
            rx.select(
                SettingsState.embedding_providers,
                value=SettingsState.selected_embedding_provider,
                on_change=SettingsState.set_selected_embedding_provider,
            ),
        ),
        
        rx.button("Save Agent Settings", on_click=SettingsState.save_agent_settings),
    )