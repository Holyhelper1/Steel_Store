import styles from "./chooser-info.module.css";
import Guarantee_logo from "../assets/Guarantee_logo.png";
import Track_logo from "../assets/Track_logo.png";
import Pointer_logo from "../assets/Pointer_logo.png";
import Sale_logo from "../assets/Sale_logo.png";
import Main_knife from "../assets/Main_knife.png";
import Ellipse from "../assets/Ellipse.png";
import { Button } from "../../Button/Button";

export const ChooserInfo = () => {
  return (
    <div className={styles.chooser_info_container}>
      <div className={styles.chooser_info_title_block}>
        <div className={styles.chooser_info_title_block_text}>
          <div>Интернет магазин сертифицированных</div>
          <div>златоустовских ножей</div>
          <p>
            Добро пожаловать на официальный сайт «ЗЛАТМАКС»! В нашем магазине
            предствлен наиболее широкий выбор Златоустовских ножей от
            Златоустовских Оружейных Фабрик и компаний, мы являемся официальными
            постовщиками.
          </p>
          <Button>Подробнее</Button>
          <p> ----- 01/4</p>
        </div>
        <div className={styles.chooser_info_title_block_img}>
          <img src={Main_knife} alt="Main_knife" />
          <img className={styles.ellipse} src={Ellipse} alt="Ellipse" />
        </div>
      </div>

      <div className={styles.chooser_info_bottom_block}>
        <div>

          
        </div>
        <div className={styles.chooser_info_bottom_block_text}>
          <div>
            <img src={Guarantee_logo} alt="Guarantee_logo" />
          </div>
          Гарантия 100% возврата денежных средств
        </div>
        <div className={styles.chooser_info_bottom_block_text}>
          <div>
            <img src={Track_logo} alt="Track_logo" />
          </div>
          Доставка по России, Казахстану и Беларусии
        </div>
        <div className={styles.chooser_info_bottom_block_text}>
          <div>
            <img src={Pointer_logo} alt="Pointer_logo" />
          </div>
          Возможность оформления заказа без регистрации
        </div>
        <div className={styles.chooser_info_bottom_block_text}>
          <div>
            <img src={Sale_logo} alt="Sale_logo" />
          </div>
          Скидки постоянным покупателям
        </div>
      </div>
    </div>
  );
};
