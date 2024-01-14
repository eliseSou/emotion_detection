const linkAngry = 'https://i.ibb.co/6nLQmGK/col-re.png'
const linkDisgust = 'https://i.ibb.co/StbDvMd/d-go-t.png'
const linkHappy = 'https://i.ibb.co/bgZ4vT4/joie.png'
const linkNeutral = 'https://i.ibb.co/Yy8Kn8B/neutre.png'
const linkFearful = 'https://i.ibb.co/vzg6pjf/peur.png'
const linkSurprised = 'https://i.ibb.co/FXVSc3h/surprise.png'
const linkSad = 'https://i.ibb.co/J3D6YPr/tristesse.png'

export enum EmotionsList {
  'angry',
  'disgust',
  'happy',
  'neutral',
  'fearful',
  'surprised',
  'sad'
}

export const EmotionsEmoticon = {
    ANGRY: linkAngry,
    DISGUST: linkDisgust,
    HAPPY: linkHappy,
    NEUTRAL: linkNeutral,
    FEARFUL: linkFearful,
    SURPRISED: linkSurprised,
    SAD: linkSad,
  } as const;