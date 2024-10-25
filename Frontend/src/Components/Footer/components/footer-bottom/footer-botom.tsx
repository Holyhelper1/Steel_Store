import styles from "./footer-bottom.module.css";
import Phone_logo from "../footer-bottom/assets/phone.png";
import Watches from "../footer-bottom/assets/Watches.png";
import GeolocationLogo from "../footer-bottom/assets/Geolocation.png";
import MailLogo from "../footer-bottom/assets/mail.png";
import Social from "../footer-bottom/assets/Social.png";
import VectorRight from "../../../Assets/Vector-right.png";
import { Button } from "../../../Button/Button";
export const FooterBottom = () => {
  return (
    <div className={styles.footer_bottom_container}>
      <div className={styles.footer_ul_container}>
        <ul>
          <li>
            <span className={styles.footer_title}> КОНТАКТЫ </span>
          </li>
          <li>
            {" "}
            <img src={Phone_logo} alt="Phone logo" /> &nbsp; 8 (800) 777-49-67
          </li>
          <li>
            {" "}
            <img src={Watches} alt="Watches" /> &nbsp; Пн-Пт 7:00 - 16:00 (МСК)
          </li>
          <li>
            <img src={GeolocationLogo} alt="Geolocation logo" /> &nbsp;
            Златоуст, ул. Шоссейная, д. 1, офис «6Б»
          </li>
          <li>
            {" "}
            <img src={MailLogo} alt="Mail logo" /> &nbsp; info@zlatmax.ru
          </li>
          <li>
            {" "}
            <img src={Social} alt="Social" />
          </li>
        </ul>
      </div>
      <div className={styles.footer_ul_container}>
        <ul>
          <li>
            <span className={styles.footer_title}> ПОЛЕЗНЫЕ ССЫЛКИ</span>
          </li>
          <li>Способы оплаты и доставки</li>
        </ul>
      </div>
      <div className={styles.footer_ul_container}>
        <ul>
          <li>
            <span className={styles.footer_title}>НАША ГАРАНТИЯ</span>
          </li>
          <li>
            Недовольны своей покупкой? Вы можете вернуть ее в течении 30 дней с
            даты получения, согласно{" "}
            <span className={styles.yellow}>нашим правилам</span>
          </li>
        </ul>
      </div>
      <div className={styles.footer_ul_container_last}>
        <ul>
          <li>
            <span className={styles.footer_title}>НОВОСТНАЯ РАССЫЛКА</span>
          </li>
          <li>Подпишитесь прямо сейчас!</li>
          <li>
            <li className={styles.emailContainer}>
              <input
                type="text"
                placeholder="example@gmail.com"
                className={styles.emailInput}
              />
              <div className={styles.emailButton}>
                <Button>
                  <img src={VectorRight} alt="Mail logo" />
                </Button>
              </div>
            </li>
          </li>
          <li className={styles.checkboxContainer}>
            <input
              type="checkbox"
              id="agreement"
              className={styles.customCheckbox}
            />
            <label htmlFor="agreement" className={styles.checkboxLabel}>
              Я прочитал Условия соглашения и согласен с условиями
            </label>
          </li>
        </ul>
      
      </div>
    </div>
  );
};
