"""Animation engine for smooth visual updates."""
from typing import Callable, Optional
from enum import Enum
import math


class AnimationType(Enum):
    """Supported animation types."""
    LINEAR = 1
    EASE_IN = 2
    EASE_OUT = 3
    EASE_IN_OUT = 4


class AnimationEngine:
    """
    Manages animations for tree visualization.
    Supports various easing functions and smooth transitions.
    """
    
    def __init__(self):
        """Initialize the animation engine."""
        self.animations = []
        self.elapsed_time = 0
    
    def create_animation(
        self,
        duration: float,
        on_update: Callable[[float], None],
        on_complete: Optional[Callable] = None,
        animation_type: AnimationType = AnimationType.EASE_IN_OUT
    ) -> 'Animation':
        """
        Create and register a new animation.
        
        Args:
            duration: Animation duration in milliseconds
            on_update: Callback function called with progress (0.0 to 1.0)
            on_complete: Optional callback called when animation completes
            animation_type: Type of easing function to use
        
        Returns:
            Animation object that was created and registered
        """
        animation = Animation(
            duration=duration,
            on_update=on_update,
            on_complete=on_complete,
            animation_type=animation_type
        )
        self.animations.append(animation)
        return animation
    
    def update(self, delta_time: float):
        """
        Update all active animations.
        
        Args:
            delta_time: Time elapsed since last update in milliseconds
        """
        self.elapsed_time += delta_time
        completed_animations = []
        
        for animation in self.animations:
            if animation.is_running:
                animation.update(delta_time)
                if animation.is_complete:
                    completed_animations.append(animation)
        
        # Remove completed animations
        for animation in completed_animations:
            self.animations.remove(animation)
    
    def stop_all(self):
        """Stop all running animations."""
        for animation in self.animations:
            animation.is_running = False
        self.animations.clear()
    
    def has_active_animations(self) -> bool:
        """Return True if there are active animations."""
        return len(self.animations) > 0
    
    def clear(self):
        """Clear all animations."""
        self.animations.clear()
        self.elapsed_time = 0


class Animation:
    """Represents a single animation."""
    
    def __init__(
        self,
        duration: float,
        on_update: Callable[[float], None],
        on_complete: Optional[Callable] = None,
        animation_type: AnimationType = AnimationType.EASE_IN_OUT
    ):
        """
        Initialize an animation.
        
        Args:
            duration: Animation duration in milliseconds
            on_update: Callback function called with progress (0.0 to 1.0)
            on_complete: Optional callback called when animation completes
            animation_type: Type of easing function to use
        """
        self.duration = duration
        self.on_update = on_update
        self.on_complete = on_complete
        self.animation_type = animation_type
        self.elapsed = 0.0
        self.is_running = True
        self.is_complete = False
    
    def update(self, delta_time: float):
        """
        Update the animation progress.
        
        Args:
            delta_time: Time elapsed since last update in milliseconds
        """
        if not self.is_running:
            return
        
        self.elapsed += delta_time
        
        if self.elapsed >= self.duration:
            # Animation complete
            self.is_complete = True
            self.is_running = False
            progress = 1.0
        else:
            # Calculate eased progress
            raw_progress = self.elapsed / self.duration
            progress = self._ease(raw_progress)
        
        # Call update callback
        self.on_update(progress)
        
        # Call complete callback if done
        if self.is_complete and self.on_complete:
            self.on_complete()
    
    def _ease(self, t: float) -> float:
        """
        Apply easing function to normalize progress.
        
        Args:
            t: Raw progress value (0.0 to 1.0)
        
        Returns:
            Eased progress value
        """
        if self.animation_type == AnimationType.LINEAR:
            return t
        elif self.animation_type == AnimationType.EASE_IN:
            return t * t
        elif self.animation_type == AnimationType.EASE_OUT:
            return t * (2 - t)
        elif self.animation_type == AnimationType.EASE_IN_OUT:
            if t < 0.5:
                return 2 * t * t
            else:
                return 1 - pow(-2 * t + 2, 2) / 2
        return t
    
    def stop(self):
        """Stop the animation."""
        self.is_running = False
        self.is_complete = True


class TransitionAnimation:
    """Helper class for animating position transitions."""
    
    @staticmethod
    def create_position_animation(
        start_x: float,
        start_y: float,
        end_x: float,
        end_y: float,
        duration: float,
        on_position_update: Callable[[float, float], None],
        on_complete: Optional[Callable] = None
    ) -> Animation:
        """
        Create an animation that smoothly transitions a position.
        
        Args:
            start_x, start_y: Starting position
            end_x, end_y: Ending position
            duration: Animation duration in milliseconds
            on_position_update: Callback with (x, y) coordinates
            on_complete: Optional completion callback
        
        Returns:
            Animation object
        """
        def update(progress: float):
            x = start_x + (end_x - start_x) * progress
            y = start_y + (end_y - start_y) * progress
            on_position_update(x, y)
        
        anim = Animation(
            duration=duration,
            on_update=update,
            on_complete=on_complete,
            animation_type=AnimationType.EASE_IN_OUT
        )
        return anim
