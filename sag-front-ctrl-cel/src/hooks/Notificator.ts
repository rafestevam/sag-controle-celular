import { NotificationType } from "@/interfaces/INotification"
import { store } from "@/store"
import { NOTIFY } from "@/store/modules/notif/constants/mutation-type"

type Notificator = {
    notify: (type: NotificationType, message: string) => void,
}

export default () : Notificator => {
    const notify = (type: NotificationType, message: string) : void => {
        store.commit(NOTIFY, {
            type,
            message,
        });
    }

    return {
        notify,
    }
}