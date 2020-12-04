from typing import Any

from .. import BaseProvider as BaseProvider

class Provider(BaseProvider):
    user_agents: Any = ...
    windows_platform_tokens: Any = ...
    linux_processors: Any = ...
    mac_processors: Any = ...
    android_versions: Any = ...
    apple_devices: Any = ...
    ios_versions: Any = ...
    def mac_processor(self): ...
    def linux_processor(self): ...
    def user_agent(self): ...
    def chrome(
        self,
        version_from: int = ...,
        version_to: int = ...,
        build_from: int = ...,
        build_to: int = ...,
    ): ...
    def firefox(self): ...
    def safari(self): ...
    def opera(self): ...
    def internet_explorer(self): ...
    def windows_platform_token(self): ...
    def linux_platform_token(self): ...
    def mac_platform_token(self): ...
    def android_platform_token(self): ...
    def ios_platform_token(self): ...