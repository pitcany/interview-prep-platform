import React, { useEffect, useState } from 'react';
import { Clock, AlertCircle } from 'lucide-react';

interface TimerProps {
  duration: number; // in seconds
  onTimeUp: () => void;
  onWarning?: (minutesLeft: number) => void;
  isPaused?: boolean;
}

export default function Timer({ duration, onTimeUp, onWarning, isPaused = false }: TimerProps) {
  const [timeLeft, setTimeLeft] = useState(duration);
  const [hasWarned10, setHasWarned10] = useState(false);
  const [hasWarned5, setHasWarned5] = useState(false);
  const [hasWarned1, setHasWarned1] = useState(false);

  useEffect(() => {
    if (isPaused || timeLeft <= 0) return;

    const interval = setInterval(() => {
      setTimeLeft((prev) => {
        const newTime = prev - 1;
        
        // Check for warnings
        if (newTime === 600 && !hasWarned10 && onWarning) {
          setHasWarned10(true);
          onWarning(10);
        }
        if (newTime === 300 && !hasWarned5 && onWarning) {
          setHasWarned5(true);
          onWarning(5);
        }
        if (newTime === 60 && !hasWarned1 && onWarning) {
          setHasWarned1(true);
          onWarning(1);
        }
        
        if (newTime <= 0) {
          clearInterval(interval);
          onTimeUp();
          return 0;
        }
        
        return newTime;
      });
    }, 1000);

    return () => clearInterval(interval);
  }, [timeLeft, isPaused, onTimeUp, onWarning, hasWarned10, hasWarned5, hasWarned1]);

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  };

  const getColorClass = () => {
    if (timeLeft <= 60) return 'text-red-500';
    if (timeLeft <= 300) return 'text-orange-500';
    if (timeLeft <= 600) return 'text-yellow-500';
    return 'text-white';
  };

  const percentage = (timeLeft / duration) * 100;

  return (
    <div className="flex items-center gap-3">
      {/* Timer display */}
      <div className={`flex items-center gap-2 ${getColorClass()}`}>
        <Clock size={20} />
        <span className="text-xl font-bold font-mono">
          {formatTime(timeLeft)}
        </span>
      </div>

      {/* Warning indicator */}
      {timeLeft <= 600 && (
        <div className="flex items-center gap-1 text-orange-500">
          <AlertCircle size={16} />
          <span className="text-sm">
            {timeLeft <= 60 ? 'Final minute!' : 
             timeLeft <= 300 ? '5 min left' : 
             '10 min left'}
          </span>
        </div>
      )}

      {/* Progress bar */}
      <div className="flex-1 max-w-xs h-2 bg-gray-700 rounded-full overflow-hidden">
        <div
          className={`h-full transition-all duration-1000 ${
            timeLeft <= 60 ? 'bg-red-500' :
            timeLeft <= 300 ? 'bg-orange-500' :
            timeLeft <= 600 ? 'bg-yellow-500' :
            'bg-blue-500'
          }`}
          style={{ width: `${percentage}%` }}
        />
      </div>
    </div>
  );
}
