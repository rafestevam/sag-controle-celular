export const b2cPolicies = {
    names: {
        signUpSignIn: "B2C_1_SAG_Controle_Cel_Auth_Sign_In",
        forgotPassword: "b2c_1_reset",
        editProfile: "b2c_1_edit_profile"
    },
    authorities: {
        signUpSignIn: {
            authority: "https://sagitbrazil.b2clogin.com/sagitbrazil.onmicrosoft.com/b2c_1_susi",
        },
        forgotPassword: {
            authority: "https://sagitbrazil.b2clogin.com/sagitbrazil.onmicrosoft.com/b2c_1_reset",
        },
        editProfile: {
            authority: "https://sagitbrazil.b2clogin.com/sagitbrazil.onmicrosoft.com/b2c_1_edit_profile"
        }
    },
    authorityDomain: "sagitbrazil.b2clogin.com"
}