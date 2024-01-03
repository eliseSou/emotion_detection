import './App.css'
import { useState } from 'react';
import { useTranslation } from "react-i18next";
import { Image, Text, Stack, useToast, HStack, VStack } from "@chakra-ui/react";

function App() {
  const { t, i18n } = useTranslation();
  const toast = useToast();

  const onClickLanguageChange = (e: any) => {
    const language = e.target.value;
    i18n.changeLanguage(language);
  }

  const [language, setLanguage] = useState("fr")

  const onOptionChange = (e: any) => {
    setLanguage(e.target.value)
  }

  return (
    <Stack className="App">
      <HStack className="custom-radio" onChange={onClickLanguageChange} spacing={25}>
        <VStack><input type="radio" name="language" value="fr" checked={language === "fr"} onChange={onOptionChange} />
          <label><Image width={50} height={35} borderRadius={10} src='https://images.assetsdelivery.com/compings_v2/iconcept123/iconcept1232203/iconcept123220300083.jpg' /></label></VStack>
        <VStack>
          <input type="radio" name="language" value="en" checked={language === "en"} onChange={onOptionChange} />
          <label><Image width={50} height={35} borderRadius={10} src='https://images.assetsdelivery.com/compings_v2/cannonzhooter/cannonzhooter2001/cannonzhooter200100001.jpg' /></label>
        </VStack>
      </HStack>

      <Text>
        {t('welcome.title')}
      </Text>
    </Stack >
  );
}

export default App;
