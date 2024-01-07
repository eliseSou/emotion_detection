import i18next from "i18next";
import { initReactI18next } from "react-i18next";

//Import all translation files
import translationEnglish from "./Translation/English/translation.json";
import translationFrench from "./Translation/French/translation.json";

//---Using different namespaces
const resources = {
    en: {
        translation: translationEnglish,
    },
    fr: {
        translation: translationFrench,
    },
}

i18next
.use(initReactI18next)
.init({
  resources,
  lng:"fr", //default language
});

export default i18next;