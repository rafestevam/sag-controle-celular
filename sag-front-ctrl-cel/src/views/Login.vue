<template>
  <div class="hero is-fullheight is-link">
    <div class="hero-body">
      <div class="container has-text-centered">
        <div class="column is-4 is-offset-4">
          <div class="box">
            <div class="box">
              <img src="@/assets/sag-dark-logo.png" width="200" />
            </div>
            <div class="title has-text-black is-5">
              GIS - Controle de Celulares
            </div>

            <Form @submit="handleLogin" :validation-schema="loginSchema" v-slot="{ errors }">
              <div class="field">
                <div class="control">
                  <Field v-model="user.username"
                    class="input is-normal"
                    type="email"
                    placeholder="E-mail"
                    name="iUsername"
                    :class="{ 'is-danger': errors.iUsername }"
                  />
                </div>
                <p class="help is-danger">{{ errors.iUsername }}</p>
              </div>
              <div class="field">
                <div class="control">
                  <Field v-model="user.password"
                    class="input is-normal"
                    type="password"
                    placeholder="Senha"
                    name="iPassword"
                    :class="{ 'is-danger': errors.iPassword }"
                  />
                </div>
                <p class="help is-danger">{{ errors.iPassword }}</p>
              </div>
              <!-- <button class="button is-block is-dark is-normal is-fullwidth">Login</button> -->
              <input type="submit" class="button is-block is-dark is-normal is-fullwidth" value="Login">
            </Form>

          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { IUsuario } from "@/interfaces/IUsuario";
import { defineComponent, ref } from "vue";
import { useStore } from "@/store";
import { Form, Field } from "vee-validate";
import * as Yup from "yup";
import { USER_LOGIN } from "@/store/modules/usuario/constants/action-type";

export default defineComponent({
  name: "LoginComponentView",
  components: {
    Form,
    Field,
  },
  data() {
    const loginSchema = Yup.object().shape({
      iUsername: Yup.string().required("O campo E-MAIL é obrigatório"),
      iPassword: Yup.string().required("O campo SENHA é obrigatório"),
    });

    return {
      loginSchema,
    }
  },
  setup(){
    const user = ref({} as IUsuario);
    const store = useStore();

    return {
      user,
      store,
    }
  },
  methods: {
    handleLogin(){
      this.store
        .dispatch(USER_LOGIN, this.user)
        .then(() => {
            this.$router.push("/home");
          })
    }
  }
});
</script>
