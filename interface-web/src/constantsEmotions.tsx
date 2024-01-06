const linkAnger = 'https://i.ibb.co/6nLQmGK/col-re.png'
const linkDisgust = 'https://i.ibb.co/StbDvMd/d-go-t.png'
const linkJoy = 'https://i.ibb.co/bgZ4vT4/joie.png'
const linkNeutral = 'https://i.ibb.co/Yy8Kn8B/neutre.png'
const linkFear = 'https://i.ibb.co/vzg6pjf/peur.png'
const linkSurprise = 'https://i.ibb.co/FXVSc3h/surprise.png'
const linkSadness = 'https://i.ibb.co/J3D6YPr/tristesse.png'

export enum EmotionsList {
  'anger',
  'disgust',
  'joy',
  'neutral',
  'fear',
  'surprise',
  'sadness'
}

export const Emotions = {
    ANGER: linkAnger,
    DISGUST: linkDisgust,
    JOY: linkJoy,
    NEUTRAL: linkNeutral,
    FEAR: linkFear,
    SURPRISE: linkSurprise,
    SADNESS: linkSadness,
  } as const;

// export const Emotions = [
//   {
//     value: linkAnger,
//     label: 'anger',
//   },
//   {
//     value: linkDisgust,
//     label: 'anger',
//   },
//   {
//     value: linkJoy,
//     label: 'joy',
//   },
//   {
//     value: linkNeutral,
//     label: 'neutral',
//   },
//   {
//     value: linkFear,
//     label: 'fear',
//   },
//   {
//     value: linkSurprise,
//     label: 'surprise',
//   },
//   {
//     value: linkSadness,
//     label: 'sadness',
//   },
// ] as const;