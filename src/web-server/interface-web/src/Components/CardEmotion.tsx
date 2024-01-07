import { EmotionsEmoticon, EmotionsList } from '../Constants/constantsEmotions';
import { VStack, Image, Text, Button, Stack } from '@chakra-ui/react'
import React, { useState, useEffect } from 'react'
import { useTranslation } from "react-i18next";

const CardEmotion = () => {
    const { t, i18n } = useTranslation();

    const refresh = () => {
        window.location.reload();
    }

    // const emotion = 'joy'   /* À décommenter pour tester la page sans fetch l'émotion */

    /* Bloc à commenter pour tester la page sans fetch l'émotion */
    const [emotion, setEmotion] = useState('');
    useEffect(() => {
        fetch("http://127.0.0.1:3002/emotion")
            .then(res => res.json())
            .then(
                (result) => {
                    try {
                        setEmotion(result["emotion"]);
                    } catch (e) {
                        throw new Error("Request object result has no 'emotion' key")
                    }
                }
            )
    })
    /* ---------------------------------------------------------- */

    const emoticonEmotion = (emotion: String) => {
        switch (emotion) {
            case EmotionsList[0]:
                return EmotionsEmoticon.ANGER;
            case EmotionsList[1]:
                return EmotionsEmoticon.DISGUST;
            case EmotionsList[2]:
                return EmotionsEmoticon.JOY;
            case EmotionsList[3]:
                return EmotionsEmoticon.NEUTRAL;
            case EmotionsList[4]:
                return EmotionsEmoticon.FEAR;
            case EmotionsList[5]:
                return EmotionsEmoticon.SURPRISE;
            case EmotionsList[6]:
                return EmotionsEmoticon.SADNESS;
        }
    }

    const srcEmotion = emoticonEmotion(emotion);

    return (
        <Stack>
            <VStack bg='#383b40' padding='5vh' borderRadius={30}>
                <Image width={500} height={500} marginBottom='2vh' src={srcEmotion} />
                <Text fontSize={25}>{t('emotion.detected')}</Text>
                <Text fontSize={35} bgGradient='linear(to-r, #FFB286, #FF0080)' bgClip='text' fontWeight='extrabold'>
                    {t('emotion.list.' + `${emotion}`)}
                </Text>
            </VStack>
            <Button onClick={refresh} bgGradient='linear(to-r, #FFB286, #FF0080)' color='white' marginTop='2vh'>
                {t('emotion.reload')}
            </Button>
        </Stack>
    )
}

export default CardEmotion;