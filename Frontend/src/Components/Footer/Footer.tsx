import { FooterBottom } from "./components/footer-bottom/footer-botom";
import { FooterRights } from "./components/footer-bottom/footer-rights/footer-rights";
import { FooterTop } from "./components/footer-top/footer-top";
import styles from "./footer.module.css";
export const Footer = () => {
  return (
    <div className={styles.footer_container}>
      <div className={styles.footer_about_web}>
        <h2>Златоустовские ножи интернет-магазин "ЗЛАТМАКС"</h2>
        <p>
          Наш интернет-магазин "ЗЛАТМАКС" предлагает Вам ножи очень высокого
          качества из города оружейников - Златоуста. Златоустовские ножи
          известны и популярны среди потребителей как на российским рынке, так и
          за рубежом: ножи охотничьи, хозяйственные, туристические, рыбацкие,
          складные и метательные. Нож Златоуста - это идеальный друг и товарищ в
          повседневной жизни и в экстремальных ситуациях. На многую продукцию
          распространяется гарантия до 10 лет - это один из главных показателей
          качества. Для Вас на нашем сайте "zlatmax" предложен огромный
          ассортимент Златоустовских ножей. Наши менеджеры помогут определиться
          и подобрать самый лучший Златоустовский нож, ориентируясь на Ваши
          пожелания.
        </p>
      </div>
      <div className={styles.footer_bottom_container}>
      <FooterTop />
    
      <FooterBottom />
      </div>
      <FooterRights />
    </div>
  );
};
