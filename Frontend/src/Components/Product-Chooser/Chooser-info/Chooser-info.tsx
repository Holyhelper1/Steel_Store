import styles from "./chooser-info.module.css";
import Guarantee_logo from "../assets/Guarantee_logo.png";
import Track_logo from "../assets/Track_logo.png";
import Pointer_logo from "../assets/Pointer_logo.png";
import Sale_logo from "../assets/Sale_logo.png";
import Main_knife from "../assets/Main_knife.png";
import Ellipse from "../assets/Ellipse.png";
import Plus from "../../Assets/Plus-logo.png";
import { Button } from "../../Button/Button";
import { useState } from "react";

export const ChooserInfo = () => {
  const [isHovered, setIsHovered] = useState(false);

  const HandleClickOpen = () => {
    setIsHovered(!isHovered);
    // setTimeout(() => setIsHovered(false), 2000);
    console.log("open text");
  };

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
          <div className={styles.chooser_info_button}>

          <Button>Подробнее</Button>
          </div>
          <p> ----- 01/4</p>
        </div>
        <div className={styles.chooser_info_title_block_img}>
          <img
            src={Main_knife}
            alt="Main_knife"
            className={styles.main_knife}
          />
          <img className={styles.ellipse} src={Ellipse} alt="Ellipse" />
          <div className={styles.chooser_info_title_block_img_plus}>
            <div
              onClick={() => HandleClickOpen()}
              className={styles.ellipse_plus}
            >
              <img src={Plus} alt="Plus" />
              {isHovered && (
                <div>
                  <p className={styles.ellipse_plus_text}>Отличные аксесуары</p>
                </div>
              )}
            </div>

            <div
              onClick={() => HandleClickOpen()}
              className={styles.knife_plus}
            >
              <img src={Plus} alt="Plus" />
              {isHovered && (
                <div>
                  <p className={styles.ellipse_plus_text}>
                    Лезвие долго держит заточку
                  </p>
                </div>
              )}
            </div>

            <div
              onClick={() => HandleClickOpen()}
              className={styles.knife_handle_plus}
            >
              <img src={Plus} alt="Plus" />
              {isHovered && (
                <div>
                  <p className={styles.ellipse_plus_text}>
                    Рукоядка на Ваш выбор
                  </p>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>

      <div className={styles.chooser_info_bottom_block}>
        <div></div>
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
