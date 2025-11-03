import { create } from 'zustand';
import type {
  User,
  UserPreferences,
  Question,
  MockInterview,
  TimerState,
  AppStore,
} from '../types';

const defaultPreferences: UserPreferences = {
  theme: 'dark',
  editorFontSize: 14,
  editorTheme: 'vs-dark',
  autoSave: true,
  showHints: true,
};

export const useAppStore = create<AppStore>((set, get) => ({
  // User
  currentUser: null,
  setCurrentUser: (user) => set({ currentUser: user }),

  // Preferences
  preferences: defaultPreferences,
  updatePreferences: (prefs) =>
    set((state) => ({
      preferences: { ...state.preferences, ...prefs },
    })),

  // Current Question
  currentQuestion: null,
  setCurrentQuestion: (question) => set({ currentQuestion: question }),

  // Mock Interview
  mockInterview: null,
  setMockInterview: (interview) => set({ mockInterview: interview }),

  // Timer
  timerState: {
    isRunning: false,
    timeRemaining: 0,
  },
  startTimer: (duration) =>
    set({
      timerState: {
        isRunning: true,
        timeRemaining: duration,
        startTime: Date.now(),
      },
    }),
  pauseTimer: () =>
    set((state) => ({
      timerState: {
        ...state.timerState,
        isRunning: false,
      },
    })),
  resetTimer: () =>
    set({
      timerState: {
        isRunning: false,
        timeRemaining: 0,
      },
    }),
}));
